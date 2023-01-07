// Convert HH:MMAM/PM to 24-hour format
const convertTo24Hour = (time) => {
  const [hours, minutesPeriod] = time.split(':')
  const [minutes, period] = minutesPeriod.split(/([A-Z]+)/)
  const hours24 = hours === '12' ? (period === 'AM' ? '00' : '12') : (period === 'AM' ? hours : (parseInt(hours) + 12).toString())

  // Pad hours and minutes with 0 if needed
  return `${hours24.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`
}
// Format all times
const dataFormatted = Object.keys(data).reduce((acc, day) => {
  const { start: inTime, end: outTime } = data[day]
  acc[day] = {
    start: convertTo24Hour(inTime),
    end: convertTo24Hour(outTime)
  }
  return acc
}, {})

const days = ['mon','tue','wed','thu','fri']
days.forEach(day => {
  document.querySelector(`#start_time_${day}`).value = dataFormatted[day]?.start
  document.querySelector(`#end_time_${day}`  ).value = dataFormatted[day]?.end
})
document.querySelector('input[name=saveSheet]').click()
