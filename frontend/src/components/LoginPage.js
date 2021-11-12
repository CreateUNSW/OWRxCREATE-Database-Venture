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
                <div className="mb-3">
                  <label for="userName" className="form-label">User Name</label>
                  <input type="email" className="form-control" id="userName" aria-describedby="emailHelp" />
                </div>
                <div className="mb-3">
                  <label for="exampleInputPassword1" className="form-label">Password</label>
                  <input type="password" className="form-control" id="exampleInputPassword1" />
                </div>
                <div className="d-grid gap-2">
                  <Link to={"/dashboard"}>
                    <button className="btn btn-primary">Submit</button>
                  </Link>
                </div>
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