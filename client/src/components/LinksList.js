import React from "react";
import { ListGroup, ListGroupItem, Container } from "reactstrap";

const Example = props => {
  return (
    <Container>
      <h4 className="mb-2">Offsetting your Carbon Footprint</h4>
      <ListGroup className="list">
        <ListGroupItem>
          <a
            href="https://blogs.ei.columbia.edu/2018/12/27/35-ways-reduce-carbon-footprint/"
            target="_blank"
          >
            A list of everyday things to do
          </a>
        </ListGroupItem>
        <ListGroupItem>
          <a
            href="https://www.americanexpress.com/en-us/business/trends-and-insights/articles/going-green-2012-sustainable-products-to-reduce-your-carbon-footprint/"
            target="_blank"
          >
            A list of sustain-ably produced products
          </a>
        </ListGroupItem>
        <ListGroupItem>
          <a
            href="https://www.goldstandard.org/take-action/offset-your-emissions"
            target="_blank"
          >
            A list of carbon offset programs to mitigate your emitted carbon
          </a>
        </ListGroupItem>
      </ListGroup>
    </Container>
  );
};

export default Example;
