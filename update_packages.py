import subprocess
from tqdm import tqdm

def update_packages():
    """
    update_packages(): Upgrade all installed Python packages to their latest version.

    This function uses the pip package manager to get a list of installed packages and their versions.
    It then loops through each package, attempts to upgrade it to the latest version, and captures any error output.
    A progress bar is displayed to track the update process.

    Returns:
    None.

    Raises:
    None.
    """

    # Get a list of installed package names and their versions
    pip_freeze_output = subprocess.check_output(['pip', 'freeze'], text=True)
    installed_packages = [line.split('==')[0] for line in pip_freeze_output.split('\n') if line.strip()]

    # Display a progress bar for the update process
    with tqdm(total=len(installed_packages), desc='loading', bar_format='{bar}', ascii=' ▋', colour='green') as progress_bar:
        for package_name in installed_packages:
            try:
                # Upgrade the package and capture any error output
                subprocess.check_call(['pip', 'install', '-U', '--quiet', package_name], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError as e:
                # If there was an error, print a message
                print(f"Error updating {package_name}: {e.stderr.strip()}")
            except KeyboardInterrupt:
                # If the user interrupts the process, print a message and exit the loop
                print("Update process was interrupted by the user.")
                break
            else:
                # If the package was successfully updated, increment the progress bar
                progress_bar.update(1)

    # Print a final message indicating the status of the update process
    if progress_bar.n == len(installed_packages):
        print(Finish!")
    else:
        print(f"Update process completed with {progress_bar.n} packages updated and {len(installed_packages) - progress_bar.n} errors.")
print("Wait the progress bar")
update_packages()
