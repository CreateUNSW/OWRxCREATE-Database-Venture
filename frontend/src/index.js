import React, { Component } from 'react'
import ReactDOM from "react-dom";
import {
  BrowserRouter,
  Switch,
  Redirect,
  Route
} from "react-router-dom";
import './scss/App.scss';
import LoginLayout from "./layouts/LoginLayout";
import AppLayout from "./layouts/AppLayout";
import LoginPage from './components/LoginPage';
import Dashboard from './components/Dashboard';
import Catalogue from './components/Catalogue';
import Purchases from './components/Purchases';
import Borrows from './components/Borrows';
import Adjustments from './components/Adjustments';
import Profile from './components/Profile';

const LoginLayoutRoute = ({ component: Component, ...rest }) => {
  return (
    <Route
      {...rest}
      render={matchProps => (
        <LoginLayout>
          <Component {...matchProps} />
        </LoginLayout>
      )}
    />
  );
};

const AppLayoutRoute = ({ component: Component, ...rest }) => {
  return (
    <Route
      {...rest}
      render={matchProps => (
        <AppLayout>
          <Component {...matchProps} />
        </AppLayout>
      )}
    />
  );
};


class App extends Component {
  render() {
    return (
      <div>
        {/* Routing Settings */}
        <BrowserRouter>
          <Switch>
            <Route exact path="/">
              <Redirect to="/login" />
            </Route>
            <LoginLayoutRoute path="/login" component={LoginPage} />
            <AppLayoutRoute path="/dashboard" component={Dashboard} />
            <AppLayoutRoute path="/catalogue" component={Catalogue} />
            <AppLayoutRoute path="/purchases" component={Purchases} />
            <AppLayoutRoute path="/borrows" component={Borrows} />
            <AppLayoutRoute path="/adjustments" component={Adjustments} />
            <AppLayoutRoute path="/profile" component={Profile} />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
