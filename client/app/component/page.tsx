"use client";

import ConsumableCard from "@/components/Consumables/ConsumableCard";
import ConsumableListingCard from "@/components/ConsumableListings/ConsumableListingCard";
import { useState, useEffect } from "react";
import Vegetable from "@/public/Vegetables.jpg";
import { userAgent } from "next/server";

export default function Page() {
  const [loading, setLoading] = useState(false);
  const [res, setRes] = useState<any>();

  return (
    <div className="m-6 flex flex-wrap gap-4">
      <ConsumableCard image={Vegetable} name="Radish" type="VEGETABLE" />
      <ConsumableCard image={Vegetable} name="Apple" type="FRUIT" />
      <ConsumableCard image={Vegetable} name="Milk" type="OTHER" />
    </div>
  );
}
