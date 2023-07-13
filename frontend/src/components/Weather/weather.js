import './weather.css'
import img from '../../loupe.svg'
import { useEffect, useState } from 'react'
import { Card } from '../Card/card'

export const Weather = () => {
  const [current, setCurrent] = useState(null)
  const [hour, setHour] = useState(null)
  const [isLoading, setLoading] = useState(false)
  const [city, setCity] = useState({city: ''})
  useEffect(() => {
    setLoading(true)
    fetch('https://weather-backend-yiwj.onrender.com/weather_current', {'credentials': 'include', 'method': 'GET'})
      .then(res => res.json())
      .then(current => {
        setCurrent(current)
        setLoading(false)
      })
  }, []);
  useEffect(() => {
    setLoading(true)
    fetch('https://weather-backend-yiwj.onrender.com/weather_3d', {'credentials': 'include', 'method': 'GET'})
      .then(res => res.json())
      .then(hour => {
        setHour(hour)
        setLoading(false)
      })
  }, []);
  const submitHandler = e => {
    e.preventDefault()

    fetch(`https://weather-backend-yiwj.onrender.com/change_city?city=${city.city}`, {
      method: 'POST',
      credentials: 'include',
      headers: {
        "Content-type": "application/json",
      }
    }).then(() => window.location.reload())

  }
  if (current != null && hour != null && current != 'Город не найден' && hour != 'Город не найден') {
    return (
      <>
      <div className="nav">
        <h1 className="logo">ЯПогода</h1>
        <form className='form' method="post" onSubmit={submitHandler}>
          <input className='input_change' placeholder='Город или село' value={city.city} onChange={e => setCity({ ...city , city: e.target.value })}></input>
        </form>
      </div>
      <div className="widget">
        <h1 className='city'>{hour[1]}</h1>
        <h2 className='temp'>{current[1]}°C</h2>
        <h2 className='desc2'>{current[3]}</h2>
        <h3 className='info2'>Погода на каждые 3 часа</h3>
        <div className='cards'>
          {hour[0].map((item => <Card date={item[0]} time={item[1]} temp={item[2]} feels_like={item[3]} desc={item[4]} wind={item[5]}/> ))}
        </div>
        
      </div>
      </>
    )
  }
  return (
    <>
    <div className="nav">
      <h1 className="logo">ЯПогода</h1>
      <form className='form' method="post" onSubmit={submitHandler}>
          <input className='input_change' placeholder='Город или село' value={city.city} onChange={e => setCity({ ...city , city: e.target.value })}></input>
      </form>
    </div>
    <div className="widget">
      Город не найден
    </div>
    </>
  )
  
}