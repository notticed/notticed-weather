import './main.css'
import { useState } from 'react'
import { useNavigate } from "react-router-dom";
import ReactLoading from 'react-loading';

export const Main = () => {
  const navigate = useNavigate();
  const [values, setValues] = useState({email: '', password: '' })
  const [isLoading, setLoading] = useState(false)
  const submitHandler = e => {
    e.preventDefault()

    setLoading(true)
    fetch('http://localhost:8000/login', {
      method: 'POST',
      credentials: 'include',
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(values),
    }).then(() => navigate('/weather'))

  }
  if (isLoading) {
  return (
    <div className="main">
      <h1 className='title'>Ярик погода</h1>
      <div className="form">
        <form className='form' method="post" onSubmit={submitHandler}>
          <input className='input' placeholder='Enter an email' type='email' value={values.email} onChange={e => setValues({ ...values, email: e.target.value })}></input>
          <input className='input' placeholder='Enter a password' value={values.password} onChange={e => setValues({ ...values, password: e.target.value })}></input>
          <button className='button'><ReactLoading className='lo' type='bars' color='#1F88DF' height={19} width={19}></ReactLoading></button>
        </form>
        <span className='info'>Если у вас нет аккаунта, то создайте его прям тут же</span>
      </div>
    </div>
  )}
  return (
    <div className="main">
      <h1 className='title'>Ярик погода</h1>
      <div className="form" method="post" onSubmit={submitHandler}>
        <form className='form'>
        <input className='input' placeholder='Enter an email' type='email' value={values.email} onChange={e => setValues({ ...values, email: e.target.value })}></input>
          <input className='input' placeholder='Enter a password' value={values.password} onChange={e => setValues({ ...values, password: e.target.value })}></input>
          <button className='button'>Войти</button>
        </form>
        <span className='info'>Если у вас нет аккаунта, то создайте его прям тут же</span>
      </div>
    </div>
  )

}