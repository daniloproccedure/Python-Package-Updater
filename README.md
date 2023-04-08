Python Package Updater

This Python script uses the pip package manager to upgrade all installed Python packages to their latest version. The script displays a progress bar to track the update process and captures any error output.

Installation
To use this script, you will need Python 3 and the tqdm package installed on your system. You can install tqdm using pip:

pip install tqdm

Functionality
The update_packages() function works by calling the pip freeze command to get a list of installed packages and their versions. It then loops through each package, attempts to upgrade it to the latest version, and captures any error output.

A progress bar is displayed to track the update process. If a package is successfully updated, the progress bar increments by one. If there is an error updating a package, the error message is printed to the console.

The update_packages() function is designed to be interruptible. If the user interrupts the update process using the keyboard, the function will stop updating packages and print a message to the console.

License
This code is released under the MIT License. See the LICENSE file for more information.
