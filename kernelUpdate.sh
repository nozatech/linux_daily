#!/bin/bash
# Update Kernel and Reboot

### Color Settings
RED="\033[1;31m"
YELLOW="\033[1;33m"
GREEN="\033[1;32m"
BOLD="\033[1m"
RESET="\033[0m"


running_kernel=$( uname -r )

# Check supported platform
if [[ "$running_kernel" != *".el"[5-7]* ]]; then
    echo -e "${RED}This script is only meant to detect vulnerable kernels on Red Hat Enterprise Linux 5, 6 and 7.${RESET}"
    exit 4
fi

# Check kernel if it is vulnerable
for tested_kernel in "${VULNERABLE_VERSIONS[@]}"; do
	if [[ "$running_kernel" == *"$tested_kernel"* ]]; then
	    vulnerable_kernel=${running_kernel}
	    break
	fi
done

# Check if kpatch is installed
modules=$( lsmod )
for tested_kpatch in "${KPATCH_MODULE_NAMES[@]}"; do
    if [[ "$modules" == *"$tested_kpatch"* ]]; then
	    applied_kpatch=${tested_kpatch}
	    break
	fi
done

# Check mitigation
mitigated=0
while read -r line; do
    if [[ "$line" == *"$MITIGATION_ON"* ]]; then
        mitigated=1
    elif [[ "$line" == *"$MITIGATION_OFF"* ]]; then
        mitigated=0
    fi
done < <( dmesg )

# Result interpretation
result=${VULNERABLE}
if (( mitigated )); then
    result=${MITIGATED}
fi
if [[ ! "$vulnerable_kernel" ]]; then
    result=${SAFE_KERNEL}
elif [[ "$applied_kpatch" ]]; then
    result=${SAFE_KPATCH}
fi

# Print result
if [[ ${result} == "$SAFE_KERNEL" ]]; then
    echo -e "${GREEN}Your kernel is ${RESET}$running_kernel${GREEN} which is NOT vulnerable.${RESET}"
    exit 0
elif [[ ${result} == "$SAFE_KPATCH" ]]; then
    echo -e "Your kernel is $running_kernel which is normally vulnerable."
    echo -e "${GREEN}However, you have kpatch ${RESET}$applied_kpatch${GREEN} applied, which fixes the vulnerability.${RESET}"
    exit 1
elif [[ ${result} == "$MITIGATED" ]]; then
    echo -e "${YELLOW}Your kernel is ${RESET}$running_kernel${YELLOW} which IS vulnerable.${RESET}"
    echo -e "${YELLOW}You have a partial mitigation applied.${RESET}"
    echo -e "This mitigation protects against most common attack vectors which are already exploited in the wild,"
    echo -e "but does not protect against all possible attack vectors."
    echo -e "Red Hat recommends that you update your kernel as soon as possible."
    exit 2
else
    echo -e "${RED}Your kernel is ${RESET}$running_kernel${RED} which IS vulnerable.${RESET}"
    echo -e "Red Hat recommends that you update your kernel. Alternatively, you can apply partial"
    echo -e "mitigation described at https://access.redhat.com/security/vulnerabilities/2706661 ."
    exit 3
fi