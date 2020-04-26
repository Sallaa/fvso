import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import './App.css';
import './App.sass';
function App() {

    const [currentTime,
        setCurrentTime] = useState(0);

    useEffect(() => {
        fetch('/time')
            .then(res => res.json())
            .then(data => {
                setCurrentTime(data.time);
            });
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo"/>
                <p>
                    Edit
                    <code>src/App.js</code>
                    and save to reload.
                </p>
                <p>The current time is {currentTime}.</p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer">
                    Learn React
                </a>
            </header>
            {/* Sass example */}
            <div className="buttons">
                <a className="button is-primary">Primary</a>
                <a className="button is-link">Link</a>
            </div>
        </div>
    );
}

export default App;
