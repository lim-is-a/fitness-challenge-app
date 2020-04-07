import React, { Component } from 'react'
import axios from 'axios';

import { Link } from 'react-router-dom';


export default class Results extends Component {
    state = {
        error: '',
        results: [],
        newResult: {
            challenge_name: "",
            name: "",
            date: "",
            time: "",
            avg_hr: 0,
            max_hr: 0,
            cals_burned: 0,
            note: ""
        },
        addResult: false
    }

    componentDidMount() {
        this.fetchResults();
    }

    fetchResults = async () => {
        try {
            const res = await axios.get('/api/v1/results/');
            this.setState({ results: res.data });
        }
        catch (err) {
            console.log(err)
            this.setState({ error: err.message })
        }
    }

    addResult = () => {
        this.setState({
            addResult: !this.state.addResult
        })
    }

    changeInput = (event) => {
        const newResultCopy = { ...this.state.newResult }
        newResultCopy[event.target.name] = event.target.value;
        this.setState({
            newResult: newResultCopy
        })
    }

    submitResultsForm = async () => {
        // This is where I'm going to post the new Result
        let form = new FormData();
        form.append("challenge_name", "4");
        form.append("name", "Lexin");
        form.append("date", "2020-01-02");
        form.append("time", "19:00");
        form.append("avg_hr", "150");
        form.append("max_hr", "189");
        form.append("cals_burned", "130");
        form.append("note", "nop");

        try {
            let request = await axios.post(`/api/v1/results/`, form, { headers: {'Content-Type': 'multipart/form-data' } }).then((res) => {
                console.log("result" + JSON.stringify(res.data))
            })
            console.log(request)
        }
        catch (error) {
            console.log("saving results caused error: " + error)
            this.setState({ error: error.message })
        }
    }

    render() {
        return (
            <div>
                <h2>Results</h2>
                <button onClick={this.addResult}>+</button>
                {this.state.addResult
                    ? <form onSubmit={this.submitResultsForm}>
                        <div>
                            Challenge Name: <input name="challenge_name" type="text" onChange={this.changeInput}></input>
                        </div>
                        <div>
                            Name: <input name="name" type="text" onChange={this.changeInput}></input>
                        </div>
                        <div>
                            Date: <input name="date" type="text" onChange={this.changeInput}></input>
                        </div>
                        <div>
                            Time: <input name="time" type="text" onChange={this.changeInput}></input>
                        </div>
                        <div>
                            Avg HR: <input name="avg_hr" type="text" onChange={this.changeInput}></input>
                        </div>
                        <div>
                            Max HR: <input name="max_hr" type="text" onChange={this.changeInput}></input>
                        </div>
                        <div>
                            Calories Burned: <input name="cals_burned" type="text" onChange={this.changeInput}></input>
                        </div>
                        <div>
                            Note: <input name="note" type="text" onChange={this.changeInput}></input>
                        </div>
                        <input type="submit" value="Submit" />
                    </form>
                    : null
                }
                {
                    this.state.results.map(result => (
                        <div key={result.id}>
                            <Link to={`/results/${result.id}/`} >{result.name}</Link>
                        </div>
                    ))
                }
            </div>
        )
    }
}
