import React, { Component } from 'react';
import axios from 'axios';
import Challenge from './Challenge';
import { Link } from 'react-router-dom';

export default class ChallengeList extends Component {
    state = {
        error: '',
        challenges:[]
    }

    componentDidMount(){
        this.fetchChallenges();
    }

    fetchChallenges = async () => {
        try {
            const res = await axios.get('/api/v1/challenges/');
            this.setState({challenges: res.data});
        }
        catch (err) {
            console.log(err)
            this.setState({error: err.message})
        }
    }

    render() {
        if (this.state.error){
            return <div>{this.state.error}</div>
        }
        return (
            <div>
                <h1>Available Challenges</h1>
                {
                    this.state.challenges.map((challenge) =>(
                        // <Link key={i} to={`challenges/${challenge.id}/`}>
                            <div key={challenge.id}>
                                <Link to={`/challenges/${challenge.id}`}> 
                                    {challenge.name}
                                </Link>
                            </div>
                        // </Link>
                    ))
                }
            </div>
        )
    }
}