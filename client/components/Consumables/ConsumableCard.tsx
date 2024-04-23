import { ReactElement } from "react";
import { ConsumableTypeString } from "@/app/lib/definitions";
export default function ConsumableCard({
  name,
  type,
  image,
}: {
  name: string;
  type: ConsumableTypeString;
  image: string;
}): ReactElement {
  return (
    <div>
      <div className="h-44 bg-fruit"></div>
    </div>
  );
}
