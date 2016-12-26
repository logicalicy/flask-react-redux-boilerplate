# Flask / React boilerplate

Boilerplate code for setting up a [Flask](http://flask.pocoo.org/) / [React](https://facebook.github.io/react/) project.
Also includes a [Webpack](https://webpack.github.io/) build and boilerplate pytests.

Made with the following tutorials and the occasional [SO](https://stackoverflow.com):

* [How To Structure Large Flask Applications](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)
* [Flask tutorial](http://flask.pocoo.org/docs/0.12/tutorial)

Install and run the Flask and React apps to get started.

## Flask app

### Install

1. Install `python`, `pip`, `virtualenv`.
2. Create virtualenv: `virtualenv env`
3. Activate it: `source env/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

### Tests

Test boilerplate provided.

```
pytest
```

### Run

To run the Flask server, run:

```python run.py```

Then, open [http://localhost:5000/api/entries/](http://localhost:5000/api/entries/) in a browser.

You should see the response:

```
[]
```

## React app

### Install

1. Install `node` and `npm`.
2. `npm install`.
3. `npm run build`.

### Run

To start the Webpack dev server, run:

```npm start```

This will run the Webpack dev server on port 8080.

With the Flask server running, open [http://localhost:5000/](http://localhost:5000/) in a browser.

You should see the "Hello World!" page.

### Develop

Change something in `app/static/js/app.js`. Changes should be reflected immediately in the browser.

## License

See [LICENSE](LICENSE).
