import { Hono } from "hono";
import { proxy } from "hono/proxy";

const proxyRoute = new Hono();

proxyRoute.post("/proxy/", (c) => {
  return c.text(c.req.url);
});

export default proxyRoute;
