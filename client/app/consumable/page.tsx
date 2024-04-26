import ConsumableListingCards from "@/sections/ConsumableListingCards";

import { ReactElement, Suspense } from "react";

function ErrorComponent(): ReactElement {
  return <div>Failed to get message...</div>;
}

export default function Page() {
  return (
    <div className="px-4 py-6 flex flex-col items-center justify-center gap-8">
      <h1 className="text-4xl font-bold text-primary-green">Consumbales</h1>

      <Suspense fallback={<div>Loading...</div>}>
        <ConsumableListingCards />
      </Suspense>
    </div>
  );
}
