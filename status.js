var underscore = require('underscore');
var async = require('async');

var JarvisError = require('./../jarvisError');
var fs = require('fs');
var registry = require('./../subsystem/registry');

module.exports.loadRoutes = function(app, prefix)
{
    // TODO: We might want to determine the health of database connections
    // for this status check.
    var versionPath = __dirname + '/../../version.txt';

    var statusHandler = function(req, res) {
        if(jarvis && jarvis.get("isCrashed")) {
            return res.send(503, 'not ok');
        }

        async.each(registry.registeredSubsystems, function(subsystemName, next) {
            var subsystem = registry[subsystemName];

            if(subsystem && subsystem.status) {
                return subsystem.status(next);
            }

            return setImmediate(next, null);
        },
        function(err) {
            if(err) {
                console.error("[StatusAPI] Subsystem health check failed", err, err.stack);
                return res.send(503, 'not ok');
            }

            return res.send(200, 'ok');
        })


    };

    var versionHandler = function(req, res) {
      fs.readFile(versionPath, 'utf8', function(err, versionText) {
         if(err) {
             console.log(err);
             res.send(500, 'Failed to read version');

         } else {
             res.send(200, versionText);
         }
      });

    };

    var testErrorHandler = function(req, res) {
        process.nextTick(function() {

            var disableDebugFunctionality = jarvisConfig.get('tcg:disableDebugFunctionality');
            if (disableDebugFunctionality === undefined) {
                disableDebugFunctionality = false;
            }

            if(disableDebugFunctionality) {
                console.warn("Debug functionality is disabled -- can't simulate async error.");
                res.sendErr(403, JarvisError("Operation not allowed."));
            } else {
                throw new Error("Something horrible happened asynchronously.");
            }

        });
    };
    app.get(prefix + '/:version/status', statusHandler);
    app.get(prefix + '/status',          statusHandler);
    app.get(prefix + '/:version/version', versionHandler);
    app.get(prefix + '/version',          versionHandler);
    app.get(prefix + '/:version/error', testErrorHandler);
    app.get(prefix + '/error', testErrorHandler);
};
