# Starlette Starter

Template repository for [Starlette][1] based applications to speed up
boilerplate setup and development.

## Built-ins
- Testing: `pytest`, and `pytest-cov` for coverage
- Database: [`databases`][2] for async database support, which uses SQLAlchemy
  internally
- Others: `ujson` for faster JSON rendering


## Setting up for development

1. Clone this repository
2. Run `pip install -r requirements.txt` (be sure to create a virtualenv before you start)
3. Install one of the following DB drivers depending on the DB you plan to use.
Note that the sqlite3 driver is installed by default for testing.
 * `pip install databases[postgresql]`
 * `pip install databases[mysql]`
4. Create a `.env` file with the following:

```
DEBUG=True
DATABASE_URL=<URL to your DB>
```

You can test that everything works with `make test`, which uses sqlite3 driver
by default.


## Development

[Starlette's documentation][1] is a good place to start if you are new to Starlette.

- API views are added in `views.py`, configure routes in `routes.py`
- New configuration settings should be set in `settings.py`
- Add database models in `models/models.py`


## Shortcuts
- `make dev`: Runs a development server
- `make test`: Runs the test suite


## License

Copyright 2020 Victor Neo

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

```
http://www.apache.org/licenses/LICENSE-2.0
```

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


[1]: https://www.starlette.io/
[2]: https://github.com/encode/databases
