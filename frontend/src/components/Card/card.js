import './card.css'

export const Card = ({date, time, temp, feels_like, desc, wind}) => {
  return (
    <>
    <div className="card">
      <h3 className='date'>{date}</h3>
      <h3 className='date'>{time}</h3>
      <h4 className='temp2'>{temp}°C</h4>
      <h4 className='desc'>{desc}</h4>
      <h5 className='info'>Ощущается как {feels_like}</h5>
      <h5 className='info'>Сила ветра {wind}</h5>
    </div>
    </>
  )
}