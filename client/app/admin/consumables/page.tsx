"use client";

import React, { useEffect, useState } from "react";
// import { cookies } from "next/headers";

const AdminConsumables = () => {
  const [consumables, setConsumables] = useState(null);

  useEffect(() => {
    const fetchConsumables = async () => {
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/consumables`, {
          method: "GET",
          //   credentials: "include",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            // Cookie: cookies().toString(),
          },
        });
        console.log("response: ", await response.json());
      } catch (err) {
        console.log("error: ", err);
      }
    };

    fetchConsumables();
  });

  return <div className="mx-auto w-11/12">Admin consu</div>;
};

export default AdminConsumables;
