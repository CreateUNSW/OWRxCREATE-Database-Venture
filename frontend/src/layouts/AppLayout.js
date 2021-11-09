import React from "react";
import {
  Link, NavLink
} from "react-router-dom";
import logo from '../resources/logo.svg'

const AppLayout = ({ children }) => {
  console.log("render");
  return (
    <>
      <div className="app-nav">
        <Link to="/dashboard" class="home-icon">
          <img src={logo} className="App-logo" alt="logo" />
        </Link>
        {/* Main Navigation */}
        <div className="nav-left">
            <NavLink to="/dashboard" activeClassName="selected">Home</NavLink>
            <NavLink to="/catalogue" activeClassName="selected">Catalogue</NavLink>
            <NavLink to="/purchases" activeClassName="selected">Purchases</NavLink>
            <NavLink to="/borrows" activeClassName="selected">Borrows</NavLink>
            <NavLink to="/adjustments" activeClassName="selected">Adjustments</NavLink>
        </div>
        {/* Profile Side Navigation */}
        <div className="nav-right">
            <NavLink to="/profile" activeClassName="selected">
              Username
              {/* <div class="profile">
                <p>username</p>
              </div> */}
            </NavLink>
        </div>
      </div>
      <div className="App">
        {children}
      </div>
    </>
  );
};

export default AppLayout;