Codebase:

You can find a simple Python codebase that calculates and displays the total price of items in a shopping cart on this GitHub repository: https://github.com/shoklah/ELU_SE_W31. Fork the project yo your GitHub account to be able to work on it. The codebase consists of a single Python script named `shopping_cart.py`. However, this script contains several issues related to code quality, potential bugs, and adherence to coding standards.

 

Tasks:

GitHub Actions Setup:
   - Navigate to the repository you forked in the previous assignment.
   - Create a new directory in the repository root named `.github/workflows`.
   - Inside this directory, create a YAML file (e.g., `ci.yml`) to configure GitHub Actions.


Automated Static Analysis:
   - Utilize the chosen static analysis tool (e.g., `pylint`, `flake8`, `bandit`) to add a step in your GitHub Actions workflow that performs automated static analysis on the `shopping_cart.py` script.
   - Configure the workflow to run the static analysis step whenever changes are pushed to the repository.

 
Automated Testing:
   - Implement a testing framework for the `shopping_cart.py` script. You can use Python's built-in `unittest` library or any other testing framework you prefer.
   - Create a testing step in the GitHub Actions workflow to execute the test suite you've created.
   - Ensure that the workflow runs the tests every time changes are pushed.

 
Submission Guidelines:


   Workflow Integration:
      - Ensure that the GitHub Actions workflow correctly executes the static analysis tool and tests as specified in the tasks.
   
   Link:
      - Provide the link to your public forked repository that demonstrates the integrated GitHub Actions workflow and includes the updated documentation.


Note: Here is the official documentation for GitHub Actions: https://docs.github.com/en/actions/quickstartLinks to an external site.
