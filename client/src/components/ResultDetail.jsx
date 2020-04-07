import React, { Component } from 'react';
import axios from 'axios';


export default class ResultDetail extends Component {
    state = {
        result:{}
    }

    componentDidMount(){

        let resultId = this.props.match.params.id
        this.fetchResult(resultId)
    }

    fetchResult = async (resultId) => {
        try {
            await axios.get(`/api/v1/results/${resultId}/`).then((response) => {
                this.setState({
                    result: response.data
                })
                console.log("MY state:::: " + JSON.stringify(this.state))
            })
        }
        catch (error) {
            console.log("getting results caused error: " + error)
            this.setState({error: error.message})
        }
    }

    render() {
        return (
            <div>
                <h1>Results</h1>
                <h5>Name: {this.state.result.name}</h5>
                <h5>Date: {this.state.result.date}</h5>
                <h5>Time: {this.state.result.time}</h5>
                <h5>Avg HR: {this.state.result.avg_hr}</h5>
                <h5>Max HR: {this.state.result.max_hr}</h5>
                <h5>Challenge Number: {this.state.result.challenge_name}</h5>
                <h5>Calories Burned: {this.state.result.cals_burned}</h5>
                <h5>Note: {this.state.result.note}</h5>
            </div>
        )
    }
}
