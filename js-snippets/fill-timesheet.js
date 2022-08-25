const days = ['mon','tue','wed','thu','fri']
days.forEach(day => {
  document.querySelector(`#start_time_${day}`).value = '09:00'
  document.querySelector(`#end_time_${day}`).value = '17:00'
})
document.querySelector('input[name=saveSheet]').click()