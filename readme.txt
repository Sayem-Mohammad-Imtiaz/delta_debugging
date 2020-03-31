::Build Instructions::

This tool has been developed with Python 3.6 in OS X environment. 

It requires no adidtional Python packages to run it. However, following command-line tools have to be available in the system this tool is being run:

1. diff
2. patch
3. patchutils

First two tools come built-in with OS X and Linux OS. However, third one has to be installed manaully. In OS X, following command can be
used for installing it: 
				
				brew install patchutils


::Project Structure::

Project directories and files are arranged in following way:

1. delta_debugging/data/ : This directory contains two versions of a target program which is to be evaluated. For detail about this two version, the bug and the changes, please read delta_debugging/data/readme.txt.

2. delta_debugging/testcase/ : This directory contains following elements:
		2.1 test_failure: A testcase for which target program fails
		2.2 test_success: A testcase which runs succesfully
		2.3 test_runner.py: This files runs the test cases to determine whether it passes or fails or remains unresolved (not compiled)

3. algorithm.py: This scripts implements both algorithm 1 and 2 from the paper identified with dd1 and dd2 methods respectively

4. delta_debug.py: This is the entry script.

5. util.py: It contains implementation related to pacthing process.



::Run Instructions::

1. Open a terminal inside delta_debugging/ folder
2. Assuming build instructions haave been met, then run following command in terminal:
			python delta_debug.py


::Interpreting Output::

The tool will print output in following order:

1. Prints detail test results for every run.
2. Total changes or configurations
3. A summary table for every run indicating which changes patched and outcome of the test case execution
4. Finally, the detected minimal bug inducing changes