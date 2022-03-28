"""
Import parameters from params.yaml
"""
import typer
import yaml
from typer import Typer

with open("params.yaml", "r") as fd:
    params = yaml.safe_load(fd)


print(params["evaluate"]["models"])
print(type(params["evaluate"]["models"]))
print(params["evaluate"]["ents"])
print(type(params["evaluate"]["ents"]))

params = params["evaluate"]

app = Typer()

@app.command()
def main(models=typer.Option(params["models"]), ents=typer.Option(params["ents"])):

    print(models)
    print(type(models))
    print(ents)
    print(type(ents))


if __name__ == "__main__":
    app()
