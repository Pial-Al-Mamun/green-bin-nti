import { serve } from "@hono/node-server";
import { Hono } from "hono";
import proxyRoute from "./routes/proxy.js";

const app = new Hono();

// Add all your route modules here
const routes = [proxyRoute] as const;

// Mount each route at the root
routes.forEach((route) => app.mount("", route));

app.get("/", (c) => c.text("Hello Hono!"));

serve(
  {
    fetch: app.fetch,
    port: 3000,
  },
  (info) => {
    console.log(`Server is running on http://localhost:${info.port}`);
  }
);
