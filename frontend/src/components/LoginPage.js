import React, { Component } from 'react';
import { Link } from "react-router-dom";

class LoginPage extends Component {
  render() {
    return (
      <div>
        <div className="login-page">
          <div className="landing-img" />
          <div className="login-form">
            <div className="login-details">
              <h1>Login</h1>
              <form>
                <label>
                  Username:
                  <input type="text" name="username" />
                </label>
                <label>
                  Password:
                  <input type="password" name="password" />
                </label>
                <Link to={"/dashboard"}>
                  <button className="btn btn-block">Login Here</button>
                </Link>
              </form>
              <div className="forget-pwd">
                <a href="#" alt="forget password">Forget Password ?</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default LoginPage;