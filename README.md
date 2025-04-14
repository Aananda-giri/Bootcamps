## Set-Up environment
 * CrewAI uses `uv` package manager (pip alternative) and 
 * Requires python 3.11 or later versions
 * `uv python install 3.12.10` install new python version
 * `uv venv --python 3.12.10` create virtual env.
 * `uv python pin 3.12.10` use specific version in current directory.

## Our FirstCrew
`crewai create` <crew-name> # create first crew
`crewai install`            # install dependencies
`uv add` <package-name>     # additional package
`crewai run`                # Run Crew AI 

### Create a new crew
* `crewai create flow guide_creator_flow`
* `cd guide_creator_flow`

### Add a new crew: Content writer crew
* `crewai flow add-crew content-crew`
* `crewai install`  # Install dependencies
* `crewai flow kickoff` # Run the flow

### Visualize the flow
* `crewai flow plot`


## References:
 - [uv docs](https://docs.astral.sh/uv/pip/environments/)
 - [CREWAI DOCS](https://docs.crewai.com/quickstart)




















## Sebastian Raschka video on virtual environments
* Managing python versions: 
  * conda
    * mamba
  * pyenv

  * Go to python.org and download new version (adopt version that is .1 or .2 version e.g. use 3.11 or 3.12)


* brew (to install python 3.11 on Mac OS):
  * brew install python@3.11

* Set up uv package manager:
  * pip3.11 install uv             # install uv
  * uv venv --python==python3.11   # create virtual environment

* activate virtual environment
  * `source .venv/bin/activate`
  * `uv pip install <package-name>`
  * `uv pip install -r requirements.txt`
