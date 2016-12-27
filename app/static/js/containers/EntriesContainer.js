import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { fetchEntries } from '../actions/entriesActions';
import EntriesComponent from '../components/EntriesComponent';
const mapStateToProps = (state) => {
    return {
        entries: state.entries.entries
    };
};
const mapDispatchToProps = (dispatch) => {
    return {
        fetchEntries: bindActionCreators(fetchEntries, dispatch)
    };
};
export default connect(mapStateToProps, mapDispatchToProps)(EntriesComponent);