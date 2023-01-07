const copy2 = copy

const timesheets = [...document.querySelector('#select2-results-1').children].map(c => c.innerText).filter(c => c !== 'Select').map(s => {

  const split = s.split(' ')
  const month = split[0]
  const startDate = new Date(split[2])
  const endDate = new Date(split[4])

  // Get short month name like "Jan"
  const startMonth = startDate.toLocaleString('en-us', { month: 'short' })
  const endMonth = endDate.toLocaleString('en-us', { month: 'short' })

  // Get day of month like "1", "31"
  const startDay = startDate.getDate()
  const endDay = endDate.getDate()

  // Concat month and day
  const start = `${startMonth} ${startDay}`
  const end = `${endMonth} ${endDay}`
  
      
  return {
    month,
    start,
    end
  }
      
})

copy2(JSON.stringify(timesheets))