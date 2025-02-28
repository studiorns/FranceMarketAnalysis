// France Market Data
const franceData = {
    impressions: {
        '2023': [23881456, 49775043, 74051417, 8598641, 23455652, 12191492, 18500158, 52823042, 28559451, 35323738, 70211063, 96375473],
        '2024': [40373079, 22711535, 31818698, 116077050, 42147321, 37674137, 53545098, 27194701, 58145869, 97294624, 99762510, 40452914],
        '2025': [67970945, 108970424, 149632907, 101925569, 73407239, 48914533, 48914533, 48914533, 33405910, 39504597, 114528721, 92820617]
    },
    travelQueries: {
        '2023': [21.0384, 18.8099, 18.546, 16.7314, 15.1316, 12.8518, 17.3182, 19.3636, 20.5083, 22.229, 24.5384, 24.8684],
        '2024': [31.2468, 28.1777, 24.072, 23.6623, 18.6417, 15.5579, 17.706, 18.794, 20.3347, 23.742, 22.6417, 23.3371],
        '2025': {
            'moderate': [26.68, 38.76, 32.98, 22.82, 22.51, 17.66, 20.92, 21.70, 20.97, 24.68, 22.59, 26.09],
            'conservative': [25.41, 36.91, 31.41, 21.73, 21.44, 16.82, 19.92, 20.67, 19.97, 23.50, 21.51, 24.85],
            'ambitious': [27.95, 40.61, 34.55, 23.91, 23.58, 18.50, 21.92, 22.73, 21.97, 25.86, 23.67, 27.33]
        }
    },
    flightSearches: {
        '2023': [4798, 1154, 1021, 1041, 1106, 935, 843, 1048, 1274, 1654, 1912, 2869],
        '2024': [4188, 3328, 2379, 1917, 1599, 1335, 1060, 1394, 1116, 1426, 1536, 1165]
    },
    hotelGuests: {
        '2023': [4798, 7431, 6326, 5209, 5679, 2917, 3232, 4457, 3611, 6767, 7653, 7885],
        '2024': [7132, 10623, 7329, 8931, 7312, 3919, 5583, 7373, 5225, 8971, 7526, 8641]
    }
};

// Months labels
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

// Chart instances
let queriesChart, impressionsChart, flightsChart, hotelChart;

// Chart configuration
const chartConfig = {
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
        mode: 'index',
        intersect: false
    },
    plugins: {
        legend: {
            position: 'bottom',
            labels: {
                usePointStyle: true,
                padding: 15,
                font: {
                    family: "'Inter', sans-serif",
                    size: 12
                }
            }
        },
        tooltip: {
            backgroundColor: 'rgba(0, 0, 0, 0.8)',
            titleFont: {
                family: "'Inter', sans-serif",
                weight: 'bold',
                size: 13
            },
            bodyFont: {
                family: "'Inter', sans-serif",
                size: 13
            },
            padding: 12,
            cornerRadius: 8,
            displayColors: true,
            usePointStyle: true,
            callbacks: {
                label: function(context) {
                    let label = context.dataset.label || '';
                    if (label) {
                        label += ': ';
                    }
                    if (context.parsed.y !== null) {
                        if (context.parsed.y > 1000000) {
                            label += (context.parsed.y / 1000000).toFixed(1) + 'M';
                        } else if (context.parsed.y > 1000) {
                            label += (context.parsed.y / 1000).toFixed(1) + 'K';
                        } else {
                            label += context.parsed.y.toLocaleString();
                        }
                    }
                    return label;
                }
            }
        }
    },
    scales: {
        x: {
            grid: {
                color: 'rgba(0, 0, 0, 0.05)'
            },
            ticks: {
                font: {
                    family: "'Inter', sans-serif",
                    size: 12
                }
            }
        },
        y: {
            beginAtZero: true,
            grid: {
                color: 'rgba(0, 0, 0, 0.05)'
            },
            ticks: {
                font: {
                    family: "'Inter', sans-serif",
                    size: 12
                }
            }
        }
    },
    elements: {
        line: {
            tension: 0.3
        },
        point: {
            radius: 3,
            hoverRadius: 6
        }
    },
    animation: {
        duration: 1000,
        easing: 'easeOutQuart'
    }
};

// Initialize charts
document.addEventListener('DOMContentLoaded', function() {
    initCharts();
    setupTabSwitching();
    setupScenarioButtons();
    setupPrintButton();
});

function initCharts() {
    // Travel Queries Chart
    const queriesCtx = document.getElementById('queries-chart').getContext('2d');
    queriesChart = new Chart(queriesCtx, {
        type: 'line',
        data: {
            labels: months,
            datasets: [
                {
                    label: '2024 Actual',
                    data: franceData.travelQueries['2024'],
                    borderColor: 'rgba(255, 159, 64, 1)',
                    backgroundColor: 'rgba(255, 159, 64, 0.1)',
                    borderWidth: 2,
                    fill: false
                },
                {
                    label: '2025 Moderate',
                    data: franceData.travelQueries['2025']['moderate'],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.1)',
                    borderWidth: 2,
                    fill: false
                }
            ]
        },
        options: {
            ...chartConfig,
            plugins: {
                ...chartConfig.plugins,
                title: {
                    display: true,
                    text: 'France Travel Queries Forecast',
                    font: {
                        family: "'Inter', sans-serif",
                        size: 16,
                        weight: 'bold'
                    },
                    padding: {
                        top: 10,
                        bottom: 20
                    }
                }
            },
            scales: {
                ...chartConfig.scales,
                y: {
                    ...chartConfig.scales.y,
                    title: {
                        display: true,
                        text: 'Travel Queries Index',
                        font: {
                            family: "'Inter', sans-serif",
                            weight: 'bold',
                            size: 13
                        }
                    }
                },
                x: {
                    ...chartConfig.scales.x,
                    title: {
                        display: true,
                        text: 'Month',
                        font: {
                            family: "'Inter', sans-serif",
                            weight: 'bold',
                            size: 13
                        }
                    }
                }
            }
        }
    });
    
    // Impressions Chart
    const impressionsCtx = document.getElementById('impressions-chart').getContext('2d');
    impressionsChart = new Chart(impressionsCtx, {
        type: 'line',
        data: {
            labels: months,
            datasets: [
                {
                    label: '2023',
                    data: franceData.impressions['2023'],
                    borderColor: 'rgba(54, 162, 235, 1)',
                    backgroundColor: 'rgba(54, 162, 235, 0.1)',
                    borderWidth: 2,
                    fill: false
                },
                {
                    label: '2024',
                    data: franceData.impressions['2024'],
                    borderColor: 'rgba(255, 206, 86, 1)',
                    backgroundColor: 'rgba(255, 206, 86, 0.1)',
                    borderWidth: 2,
                    fill: false
                },
                {
                    label: '2025 (Planned)',
                    data: franceData.impressions['2025'],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.1)',
                    borderWidth: 2,
                    fill: false
                }
            ]
        },
        options: {
            ...chartConfig,
            plugins: {
                ...chartConfig.plugins,
                title: {
                    display: true,
                    text: 'France Media Impressions',
                    font: {
                        family: "'Inter', sans-serif",
                        size: 16,
                        weight: 'bold'
                    },
                    padding: {
                        top: 10,
                        bottom: 20
                    }
                }
            },
            scales: {
                ...chartConfig.scales,
                y: {
                    ...chartConfig.scales.y,
                    title: {
                        display: true,
                        text: 'Impressions',
                        font: {
                            family: "'Inter', sans-serif",
                            weight: 'bold',
                            size: 13
                        }
                    },
                    ticks: {
                        callback: function(value) {
                            if (value >= 1000000) return (value / 1000000).toFixed(1) + 'M';
                            if (value >= 1000) return (value / 1000).toFixed(1) + 'K';
                            return value;
                        }
                    }
                },
                x: {
                    ...chartConfig.scales.x,
                    title: {
                        display: true,
                        text: 'Month',
                        font: {
                            family: "'Inter', sans-serif",
                            weight: 'bold',
                            size: 13
                        }
                    }
                }
            }
        }
    });
    
    // Flight Searches Chart
    const flightsCtx = document.getElementById('flights-chart').getContext('2d');
    flightsChart = new Chart(flightsCtx, {
        type: 'line',
        data: {
            labels: months,
            datasets: [
                {
                    label: '2023',
                    data: franceData.flightSearches['2023'],
                    borderColor: 'rgba(54, 162, 235, 1)',
                    backgroundColor: 'rgba(54, 162, 235, 0.1)',
                    borderWidth: 2,
                    fill: false
                },
                {
                    label: '2024',
                    data: franceData.flightSearches['2024'],
                    borderColor: 'rgba(255, 159, 64, 1)',
                    backgroundColor: 'rgba(255, 159, 64, 0.1)',
                    borderWidth: 2,
                    fill: false
                }
            ]
        },
        options: {
            ...chartConfig,
            plugins: {
                ...chartConfig.plugins,
                title: {
                    display: true,
                    text: 'France Flight Searches',
                    font: {
                        family: "'Inter', sans-serif",
                        size: 16,
                        weight: 'bold'
                    },
                    padding: {
                        top: 10,
                        bottom: 20
                    }
                }
            },
            scales: {
                ...chartConfig.scales,
                y: {
                    ...chartConfig.scales.y,
                    title: {
                        display: true,
                        text: 'Flight Searches',
                        font: {
                            family: "'Inter', sans-serif",
                            weight: 'bold',
                            size: 13
                        }
                    }
                },
                x: {
                    ...chartConfig.scales.x,
                    title: {
                        display: true,
                        text: 'Month',
                        font: {
                            family: "'Inter', sans-serif",
                            weight: 'bold',
                            size: 13
                        }
                    }
                }
            }
        }
    });
    
    // Hotel Guests Chart
    const hotelCtx = document.getElementById('hotel-chart').getContext('2d');
    hotelChart = new Chart(hotelCtx, {
        type: 'line',
        data: {
            labels: months,
            datasets: [
                {
                    label: '2023',
                    data: franceData.hotelGuests['2023'],
                    borderColor: 'rgba(54, 162, 235, 1)',
                    backgroundColor: 'rgba(54, 162, 235, 0.1)',
                    borderWidth: 2,
                    fill: false
                },
                {
                    label: '2024',
                    data: franceData.hotelGuests['2024'],
                    borderColor: 'rgba(255, 159, 64, 1)',
                    backgroundColor: 'rgba(255, 159, 64, 0.1)',
                    borderWidth: 2,
                    fill: false
                }
            ]
        },
        options: {
            ...chartConfig,
            plugins: {
                ...chartConfig.plugins,
                title: {
                    display: true,
                    text: 'France Hotel Guests',
                    font: {
                        family: "'Inter', sans-serif",
                        size: 16,
                        weight: 'bold'
                    },
                    padding: {
                        top: 10,
                        bottom: 20
                    }
                }
            },
            scales: {
                ...chartConfig.scales,
                y: {
                    ...chartConfig.scales.y,
                    title: {
                        display: true,
                        text: 'Hotel Guests',
                        font: {
                            family: "'Inter', sans-serif",
                            weight: 'bold',
                            size: 13
                        }
                    }
                },
                x: {
                    ...chartConfig.scales.x,
                    title: {
                        display: true,
                        text: 'Month',
                        font: {
                            family: "'Inter', sans-serif",
                            weight: 'bold',
                            size: 13
                        }
                    }
                }
            }
        }
    });
}

function setupTabSwitching() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Update active tab button
            tabButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Update active tab content
            const tabId = this.getAttribute('data-tab');
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(`${tabId}-tab`).classList.add('active');
        });
    });
}

function setupScenarioButtons() {
    const scenarioButtons = document.querySelectorAll('.scenario-btn');
    scenarioButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Update active button
            scenarioButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Update chart based on selected scenario
            updateQueriesChart(this.getAttribute('data-scenario'));
        });
    });
}

function updateQueriesChart(scenario) {
    // Clear existing datasets
    queriesChart.data.datasets = [];
    
    if (scenario === 'actual') {
        // Show 2023 and 2024 actual data
        queriesChart.data.datasets.push({
            label: '2023 Actual',
            data: franceData.travelQueries['2023'],
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor: 'rgba(54, 162, 235, 0.1)',
            borderWidth: 2,
            fill: false
        });
        
        queriesChart.data.datasets.push({
            label: '2024 Actual',
            data: franceData.travelQueries['2024'],
            borderColor: 'rgba(255, 159, 64, 1)',
            backgroundColor: 'rgba(255, 159, 64, 0.1)',
            borderWidth: 2,
            fill: false
        });
    } else {
        // Show 2024 actual and 2025 forecast for selected scenario
        queriesChart.data.datasets.push({
            label: '2024 Actual',
            data: franceData.travelQueries['2024'],
            borderColor: 'rgba(255, 159, 64, 1)',
            backgroundColor: 'rgba(255, 159, 64, 0.1)',
            borderWidth: 2,
            fill: false
        });
        
        queriesChart.data.datasets.push({
            label: `2025 ${scenario.charAt(0).toUpperCase() + scenario.slice(1)}`,
            data: franceData.travelQueries['2025'][scenario],
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.1)',
            borderWidth: 2,
            fill: false
        });
    }
    
    // Update chart
    queriesChart.update();
}

function setupPrintButton() {
    const printBtn = document.querySelector('.print-btn');
    if (printBtn) {
        printBtn.addEventListener('click', function() {
            window.print();
        });
    }
    
    const exportBtn = document.querySelector('.export-btn');
    if (exportBtn) {
        exportBtn.addEventListener('click', function() {
            // Export functionality would go here
            alert('Export functionality would be implemented here.');
        });
    }
}
