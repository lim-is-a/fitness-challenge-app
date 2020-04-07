import React, { Component } from "react";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import ChallengeList from "./components/ChallengeList";
import Challenge from "./components/Challenge";
import Results from "./components/Results";
import ResultDetail from "./components/ResultDetail";
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
                            <div><Link to="/results/">Results</Link></div>
                        </div>
                    </div>

                    <Switch>
                        <Route exact path="/" component={ChallengeList} />
                        <Route path="/challenges/:id" component={Challenge} />
                        <Route exact path="/results/" component={Results} />
                        <Route path="/results/:id" component={ResultDetail} />
                    </Switch>
                </div>
            </Router>
        );
    }
}

export default App;
