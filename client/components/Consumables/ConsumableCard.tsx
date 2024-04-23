import { ReactElement } from "react";

export default function ConsumableCard({
  name,
  type,
  image,
}: {
  name: string;
  type: ConsumableType;
  image: string;
}): ReactElement {
  return <div>Hello World</div>;
}
