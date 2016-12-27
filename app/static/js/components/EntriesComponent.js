import React, {
    PropTypes
} from 'react';

class EntriesComponent extends React.Component {
    componentDidMount() {
        this.props.fetchEntries();
    }
    render() {
        const entries = this.props.entries;
        if (entries.length === 0) {
            return (
                <h2>No entries</h2>
            );
        }
        const entryRows = entries.map((entry) => {
            return (
                <div key={entry.id} className="entries__entry">
                    <h3>{entry.title}</h3>
                    <p>{entry.text}</p>
                </div>
            );
        });
        return (
            <div className="entries">
                {entryRows}
            </div>
        );
    }
};

EntriesComponent.propTypes = {
    entries: PropTypes.array.isRequired,
    fetchEntries: PropTypes.func.isRequired
};

export default EntriesComponent;