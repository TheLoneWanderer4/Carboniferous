class TripTable extends React.Component {
  onClick = () => {
    this.props.requestMap({
      start: "Tucson",
      end: "Dallas",
      mode: "car"
    });
  };

  render() {
    console.log(this.props.paths);
    console.log(this.props.link);

    return (
      <div>
        <Button onClick={this.onClick}> Test </Button>
        <iframe
          width="600"
          height="450"
          frameBorder="0"
          src={this.props.link}
          allowFullScreen
        ></iframe>
      </div>
    );
  }
}
