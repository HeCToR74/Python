import React from "react";
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Button from '@material-ui/core/Button';
import {MapFrame} from "src/components/map/MapFrame";
import axios from 'axios';
import { API_KEY } from 'src/constants.js';


export class MapModal extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      latitude: 48.29083,
      longitude: 25.93444,
    };
  }

  handleMapClick(event){
    this.setState({latitude: event.latLng.lat(),
                         longitude: event.latLng.lng()})
  }

  handleSubmit(){
    axios('https://api.opencagedata.com/geocode/v1/json?q='+
          this.state.latitude+'%2C%20'+this.state.longitude
          +'&key='+API_KEY+'&language=en&pretty=1')
      .then(response => {
        const {road, house_number} = response.data.results[0].components;
            this.props.onSubmit({lat: this.state.latitude,
                              lng: this.state.longitude}, `${road}, ${house_number}`);
      });

  }

  render() {
    return (
      <Dialog
        open={this.props.open}
        onClose={this.props.onClose}
        fullWidth={true}
      >
        <DialogTitle>
          Location selection
        </DialogTitle>
        <DialogContent>
          <DialogContentText>
            <MapFrame
              defaultCenter={{lat: this.state.latitude, lng: this.state.longitude}}
              markerPosition={{lat: this.state.latitude, lng: this.state.longitude}}
              onClick={this.handleMapClick.bind(this)}
            >
            </MapFrame>
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button
            onClick={this.props.onClose}
            color="primary" >
            Cancel
          </Button>
          <Button
            onClick={this.handleSubmit.bind(this)}
            color="secondary"
            autoFocus >
            Save
          </Button>
        </DialogActions>
      </Dialog>
    );
  }
}