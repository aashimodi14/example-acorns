# Flask sample application

## Python/Flask application

Project structure:
```
.
├── Acornfile
├── app
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── compose.yaml
└── README.md

```

[_Acornfile_](.Acornfile)
```
args: {
  // Configure your personal welcome text
  welcome: "Acorn User!!"
}
containers: {
  web: {
    build: {
      context: "app"
      target: "builder"
    }
   env: {
      "WELCOME": args.welcome
      if args.dev { 
        "FLASK_ENV": "development"
        "FLASK_DEBUG" : "1"
         }
    }
    if args.dev { dirs: "/app": "./" }
    ports: publish: "8000/http"
  }
}
```

## Deploy with Acorn

To deploy this project, go to 

```bash
  acorn run
```

## Explaining the Acornfile

* `args` section: describes a set of arguments that can be passed in by the user of this Acorn image

A help text will be auto-generated using the comment just above the arg:


```bash
$ acorn run . --help

Volumes:   <none>
Secrets:   <none>
Containers: web
Ports:     web:8000/http

      --welcome-text string   Configure your personal welcome text
```

* `containers` section: describes the set of containers your Acorn app consists of

  * Note: app, db and cache are custom names of your containers
  * `app` - Our Python Flask App
    * `build`: build from Dockerfile that we created
    * `env`: environment variables, statically defined, referencing a secret or referencing an Acorn argument
    * `ports`: using the publish type, we expose the app inside the cluster but also outside of it using an auto-generated ingress resource
    * `dirs`: Directories to mount into the container filesystem
      * `dirs: "/app": "./"`: Mount the current directory to the /app dir, which is where the code resides inside the container as per the Dockerfile. This is to enable hot-reloading of code.

## Run your Application

To start your Acorn app just run:

```bash
acorn run -n flask-app . 
```

or customize the welcome text argument via:

```bash
acorn run -n flask-app . --welcome "Let's Get Started"
```

The `-n flask-app` gives this app a specific name so that the rest of the steps can refer to it. If you omit `-n`, a random two-word name will be generated.

## Access your app

Due to the configuration `ports: publish: "8000/http"` under `containers.app`, our web app will be exposed outside of our Kubernetes cluster using the cluster's ingress controller. Checkout the running apps via

```bash
acorn apps
```

```bash
$ acorn apps
NAME        IMAGE          COMMIT         CREATED     ENDPOINTS                                          MESSAGE
flask-app   0ed9a2b95c69   114c50666ed9   3m22s ago   http://web-flask-app-98d916c5.local.oss-acorn.io   OK

```

## Development Mode

In development mode, Acorn will watch the local directory for changes and synchronize them to the running Acorn app. In general, changes to the Acornfile are directly synchronized, e.g. adding environment variables, etc. Depending on the change, the deployed containers will be recreated.

```bash
acorn dev -n flask-app
```

The lines `if args.dev { dirs: "/app": "./" }` enable hot-reloading of code by mounting the current local directory into the app container.

You will see the change applied when you reload the application's page in your browser.


