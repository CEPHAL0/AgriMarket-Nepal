"use client";

import ConsumableCard from "@/components/Consumables/ConsumableCard";
import { useState, useEffect } from "react";
import Vegetable from "@/public/Vegetables.jpg";
import { fetchConsumables } from "./fetchConsumables";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function Page() {
  const [res, setRes] = useState<any>();

  useEffect(() => {
    getConsumables()
      .then((data) => {
        setRes(data);
      })
      .catch((error) => {
        console.log(error.message);
      });
  }, []);

  return (
    <div className="px-4 py-6 flex flex-col items-center justify-center gap-8">
      <h1 className="text-4xl font-bold text-primary-green">Consumbales</h1>
      {res ? (
        <div className="flex flex-wrap justify-center content-start gap-10 w-full">
          {res.map((consumable: any) => {
            return (
              <ConsumableCard
                key={consumable.id}
                image={`${API_URL}/${consumable.image_path}`}
                name={consumable.name}
                type={consumable.type}
              />
            );
          })}
        </div>
      ) : (
        "Loading..."
      )}
    </div>
  );
}

export async function getConsumables() {
  let data = await fetchConsumables();
  return data;
}
