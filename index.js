function readData(file, callback) {
  var rawFile = new XMLHttpRequest()
  rawFile.overrideMimeType('application/json')
  rawFile.open('GET', file, true)
  rawFile.onreadystatechange = function () {
    if (rawFile.readyState === 4 && rawFile.status == '200') {
      callback(rawFile.responseText)
    }
  }
  rawFile.send(null)
}

//usage:
readData('/MASTER.json', function (text) {
  document.getElementById('devices').innerHTML = renderDevices(JSON.parse(text))
})

renderDevices = (data) => {
  let result = Object.keys(data)
    .map(function (key, index) {
      return `
    <div onclick="toggleView(this)" class="node">
    <img src="/images/laptop-icon.png">
    <div class="data" style='background:${data[key]['Status'] === 'Online' && '#3ce33c'}'>
    ${data[key]['IP']}
    <br>
    ${data[key]['MAC Address']}
    <br>
    ${data[key]['Status']}
    </div> 
    <div class="pcline"></div>
    </div>
    
    ${(index) % 5 === 0 ? `
    <div class='device-line' style='top:${(140 * (((index) / 5) + 1)+220)}px'></div>
    `: ''}

    `
    })
    .join(' ')

  return result
}

toggleView = (e) => {
  if (e.className === 'node show') {
    e.classList.remove('show')
  } else {
    e.classList.add('show')
  }
}
