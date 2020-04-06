import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

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
            // console.log("response::: " + res.data)
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
                    this.state.challenges.map(challenge =>(
                        <div key={challenge.id}>
                            <Link to={`/challenge/${challenge.id}`}>
                                <div>
                                    {challenge.name}
                                    <img src={challenge.image_url} alt="image unavailable"/>
                                    
                                </div>
                            </Link>
                        </div>
                    ))
                }
            </div>
        )
    }
}

