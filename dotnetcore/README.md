# .NET 7 Hello World

This sample demonstrates a tiny Hello World .NET Core app

[_Acornfile_](.Acornfile)
```
containers: {
  web: {
    build: {
      context: "."
      dockerfile: "./Dockerfile.linux"
    }
   env: {
      if args.dev { 
        "ASPNETCORE_ENVIRONMENT": "development"
      }
   }
    ports: publish: "80/http"
  }
}
```

## Deploy with Acorn

To deploy this project, go to 

```bash
acorn run -n web-app
```

## Explaining the Acornfile

* `containers` section: describes the set of containers your Acorn app consists of

  * Note: app, db and cache are custom names of your containers
  * `web` - Our .NET7 App
    * `build`: build from Dockerfile that we created
    * `env`: environment variables, statically defined, referencing a secret or referencing an Acorn argument
    * `ports`: using the publish type, we expose the app inside the cluster but also outside of it using an auto-generated ingress resource

## Access your app

Due to the configuration `ports: publish: "80/http"` under `containers.app`, our web app will be exposed outside of our Kubernetes cluster using the cluster's ingress controller. Checkout the running apps via

```bash
acorn apps
```

```bash
$ acorn apps
NAME       IMAGE          COMMIT         CREATED   ENDPOINTS                                         MESSAGE
shy-snow   64913f1b2b4e   7a52ee67c381   4m ago    http://web-shy-snow-dc4264a9.local.oss-acorn.io   OK

```

## Development Mode

In development mode, Acorn will watch the local directory for changes and synchronize them to the running Acorn app. In general, changes to the Acornfile are directly synchronized, e.g. adding environment variables, etc. Depending on the change, the deployed containers will be recreated.

```bash
acorn dev -n web-app
```

