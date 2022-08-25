const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));
const copy2 = copy

async function copyCreds() {
  document.querySelector('portal-application').click()
  await wait(1000)
  document.querySelectorAll('portal-instance')[1].children[0].children[0].click()
  await wait(3000)
  document.querySelector('#temp-credentials-button').click()
  await wait(1000)
  const vars = [... document.querySelectorAll('.code-line')]
    .slice(0,3)
    .map(el => el.innerText).join('\n')
    
  copy2(vars)
}

copyCreds()