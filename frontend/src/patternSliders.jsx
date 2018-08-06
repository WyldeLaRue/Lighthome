

// Shoutout to https://github.com/iozbeyli/react-semantic-ui-range/blob/master/lib/elements/slider.js


import React,{Component} from 'react';
import { Slider } from 'react-semantic-ui-range'

export default class SliderTest extends Component{
  constructor(props){
    super(props);
    this.state={
      value1: 4,
      value: 0
    }
  }
 
  handleValueChange(e, {value}){
    this.setState({
      value: value
    })
  }
 
  render(){
    const settings = {
      start:2,
      min:0,
      max:10,
      step:1,
    }return (
      <Grid padded>
        <Grid.Column width={16}>
          <Segment>
            <h1>Discrete</h1>
            <p>
              <Slider discrete color="red" inverted={false} settings={settings}/>
            </p>
          </Segment>
        </Grid.Column>
        <Grid.Column width={16}>
          <Segment>
           <h1>Callback!</h1>
            <p>
              <Slider color="red" inverted={false}
                settings={{
                start: this.state.value1,
                min:0,
                max:10,
                step:1,
                onChange: (value) => {
                  this.setState({
                    value1:value
                  })
                }
              }}/>
            </p>
            <Label color="red">{this.state.value1}</Label>
          </Segment>
        </Grid.Column>
        <Grid.Column width={16}>
          <Segment>
            <h1>Disabled!</h1>
            <p>
              <Slider color="red" disabled inverted={false} settings={{
                start: this.state.value1,
                min:0,
                max:10,
                step:1,
                onChange: (value) => {
                  this.setState({
                    value1:value
                  })
                },
              }}/>
            </p>
          </Segment>
        </Grid.Column>
        <Grid.Column width={16}>
        <Segment>
          <h1>Controlled</h1>
          <p>
              <Slider value={this.state.value} color="red" inverted={false} settings={settings}/>
            </p>
            <Input placeholder="Enter Value" onChange={this.handleValueChange.bind(this)}/>
        </Segment>
      </Grid.Column>
    )
  }
}
