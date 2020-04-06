import React, {Component} from "react";
import {BrowserRouter as Router, Route, Switch, Link} from "react-router-dom";
import ChallengeList from "./components/ChallengeList";
import Challenge from "./components/Challenge";
import "./App.css";

class App extends Component {
    render() {
        return (
            <Router>
                <div className="App">

                    <div>
                        <h1>Fitness Challenge</h1>
                        <div>
                            <div><Link to="/">All Challenges</Link></div>
                        </div>
                    </div>

                    <Switch>
                      <Route exact path="/" component={ChallengeList}/>
                      <Route path="/challenge/:id" component={Challenge}/>
                    </Switch>
                </div>
            </Router>
        );
    }
}

export default App;
