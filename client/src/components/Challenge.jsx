import React, { Component } from 'react'
import axios from 'axios';

export default class Challenge extends Component {
    state = {
            challenge: {},

    }

    componentDidMount(){
        const challengeId = this.props.match.params.id;
        this.fetchChallenge(challengeId)
    }

    fetchChallenge = async (challengeId) => {
        try {
            await axios.get(`/api/v1/challenges/${challengeId}/`).then((Response) => {
                this.setState({
                    challenge: Response.data
                })
                console.log("MY state:::: " + JSON.stringify(this.state))
            })
        }
        catch (error) {
            console.log(error)
            this.setState({error: error.message})
        }
    }

    render() {
        return (
            <div>
                <h1>Name: {this.state.challenge.name}</h1>
                <img src={this.state.challenge.image_url} alt="unavailable"/>
                <h5>Excercises: </h5>
                {
                    this.state.challenge.exerciseList
                    ?
                    this.state.challenge.exerciseList.map((exercise) =>(
                        <div key={exercise.id}>
                            <h5>Name: {exercise.name}</h5>
                            <img src={exercise.image_url}></img>
                            <p>Description: {exercise.description}</p>
                        </div>
                    ))
                    : ""
                }
            </div>
        )
    }
}

