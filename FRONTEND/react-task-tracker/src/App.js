import Header from "./components/Header";
import Tasks from './components/Tasks'
import {useState} from 'react'

function App() {
  const [tasks, setTasks] = useState(
    [
      {
        id: 1,
        text: "exam 1",
        day: "Feb 6th at 1:30 PM",
        reminder: true,
      },
      {
        id: 2,
        text: "exam 2",
        day: "Feb 8th at 9:30 PM",
        reminder: true,
      },
      {
        id: 3,
        text: "exam 3",
        day: "Feb 13th at 12:00 PM",
        reminder: true,
      }
    ]
  )

  return (
    <div className="container">
      <Header />
      <Tasks tasks = {tasks}/>
    </div>
  );
}

export default App;
