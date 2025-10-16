import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  component: App,
});

function App() {
  return (
    <div className="flex items-center flex-1 justify-center h-screen">
      <img src="http://localhost:8000/video" alt="Camera Feed" />
    </div>
  );
}
