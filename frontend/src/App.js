import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <p>
                Something like this
            </p>
        );
    }
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);