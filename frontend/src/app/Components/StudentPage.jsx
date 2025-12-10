"use client";
import { useEffect, useState } from "react"

export default function StudentPage(){
    const [studentData, setStudentData] = useState([])
    

    useEffect(()=>{
        const fetchStudents = async() =>{
            try{
                const res = await fetch("http://127.0.0.1:8000/api/students/")
                if(res.ok){
                    const studentDataFromApi = await res.json()
                    console.log(studentDataFromApi)
                    setStudentData(studentDataFromApi)
                }
                else{
                    console.error("Something went wrong")
                }
            }catch(e){
                console.error(e.message)
            }
        }
        fetchStudents()
    },[])
    return(
        <div>
            <ul>
                {studentData.map((sdata)=>(
                    <li key={sdata.id}>Student name : {sdata.first_name}</li>
                ))}
            </ul>

        </div>
    )
}