import React, {Component} from "react";
import Radium, {StyleRoot} from 'radium';
import {bounceInRight} from 'react-animations';
import {bounceInLeft} from 'react-animations';
import {bounceInDown} from 'react-animations';
import {bounceInUp} from 'react-animations';
import './counter.css';

class Counter extends Component {
    state = {
        count: 1,
        throwError: false
    };



    render() {
        const styles = {
            bounceR: {
                animation: 'x 3.2s',
                animationName: Radium.keyframes(bounceInRight, 'bounce'),

            },
            bounceL: {
                animation: 'x 2.5s',
                animationName: Radium.keyframes(bounceInLeft, 'bounce'),

            },
            bounceD: {
                animation: 'x 2.2s',
                animationName: Radium.keyframes(bounceInDown, 'bounce'),

            },
            bounceU: {
                animation: 'x 2s',
                animationName: Radium.keyframes(bounceInUp, 'bounce'),

            }
        }

        return (
            <div id="defd">
                <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
                <button onClick={this.handleIncrement} className="btn btn-secondary btn-sm">Increment</button>
                <button onClick={this.handleDecrement} className="btn btn-secondary btn-sm">Decrement</button>
                <StyleRoot><h1 style={this.state.throwError ? styles.bounceR : null} id="error">{this.errorMessage()}</h1></StyleRoot>
                <StyleRoot><h1 style={this.state.throwError ? styles.bounceL : null} id="error">{this.errorMessage()}</h1></StyleRoot>
                <StyleRoot><h1 style={this.state.throwError ? styles.bounceD : null} id="error">{this.errorMessage()}</h1></StyleRoot>
                <StyleRoot><h1 style={this.state.throwError ? styles.bounceU : null} id="error">{this.errorMessage()}</h1></StyleRoot>
            </div>
        );

    }


    handleIncrement = () => {
        if (this.state.count < 10) {
            this.setState({count: this.state.count + 1});
        }
        else {
            this.setState({error: this.state.throwError = true})
        }
    }

    errorMessage() {
        if (this.state.throwError) {
            return 'Fuck you'
        }
    }


    handleDecrement = () => {
        if (this.state.count > 0) {
            this.setState({count: this.state.count - 1});
        }
        else {
            this.setState({error: this.state.throwError = true})
        }
    }

    getBadgeClasses() {
        let classes = "badge m-2 badge-";
        classes += (this.state.count === 0) ? "warning" : "primary";
        return classes;
    }

    formatCount() {
        const {count} = this.state;
        return count === 0 ? <h1>Zero</h1> : <h1>{count}</h1>;
    }

}

export default Counter;