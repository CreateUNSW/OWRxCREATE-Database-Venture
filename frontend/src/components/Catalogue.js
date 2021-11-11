import React from 'react'
import {
    Link
  } from "react-router-dom";

const Catalogue = () => {
    return (
        <div>
            <h1>Catalogue</h1>
            <div className="card-grids-media four-cards retain-two">
                <Link to="/catalogue/parts">
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                </Link>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
                <div className="grid-card">
                    <p>Parts</p>
                </div>
            </div>
        </div>
    )
}

export default Catalogue;