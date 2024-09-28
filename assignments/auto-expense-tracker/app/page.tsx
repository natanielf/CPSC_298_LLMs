'use client'

import { useState, useEffect } from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { PlusIcon, TrashIcon } from 'lucide-react'

type Expense = {
  id: string
  date: string
  description: string
  amount: number
}

export default function AutoExpenseTracker() {
  const [expenses, setExpenses] = useState<Expense[]>([])
  const [date, setDate] = useState('')
  const [description, setDescription] = useState('')
  const [amount, setAmount] = useState('')
  const [theme, setTheme] = useState<'light' | 'dark'>('light')

  useEffect(() => {
    const storedExpenses = localStorage.getItem('autoExpenses')
    if (storedExpenses) {
      setExpenses(JSON.parse(storedExpenses))
    }
  }, [])

  const addExpense = (e: React.FormEvent) => {
    e.preventDefault()
    const newExpense: Expense = {
      id: Date.now().toString(),
      date,
      description,
      amount: parseFloat(amount)
    }
    const updatedExpenses = [...expenses, newExpense]
    setExpenses(updatedExpenses)
    localStorage.setItem('autoExpenses', JSON.stringify(updatedExpenses))
    setDate('')
    setDescription('')
    setAmount('')
  }

  const deleteExpense = (id: string) => {
    const updatedExpenses = expenses.filter(expense => expense.id !== id)
    setExpenses(updatedExpenses)
    localStorage.setItem('autoExpenses', JSON.stringify(updatedExpenses))
  }

  const totalExpenses = expenses.reduce((sum, expense) => sum + expense.amount, 0)

  return (
    <div className="container mx-auto p-4">

      <Card className="mb-6">
        <CardHeader>
          <CardTitle>Add New Expense</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={addExpense} className="space-y-4">
            <div>
              <Label htmlFor="date">Date</Label>
              <Input
                id="date"
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
                required
              />
            </div>
            <div>
              <Label htmlFor="description">Description</Label>
              <Input
                id="description"
                type="text"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                required
              />
            </div>
            <div>
              <Label htmlFor="amount">Amount ($)</Label>
              <Input
                id="amount"
                type="number"
                step="0.01"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                required
              />
            </div>
            <Button type="submit">
              <PlusIcon className="mr-2 h-4 w-4" /> Add Expense
            </Button>
          </form>
        </CardContent>
      </Card>

      <Card className="mb-6">
        <CardHeader>
          <CardTitle>Expense List</CardTitle>
        </CardHeader>
        <CardContent>
          <ul className="space-y-2">
            {expenses.map((expense) => (
              <li key={expense.id} className="flex justify-between items-center border-b py-2">
                <div>
                  <span className="font-semibold">{expense.date}</span> - {expense.description}
                </div>
                <div className="flex items-center">
                  <span className="mr-4">${expense.amount.toFixed(2)}</span>
                  <Button variant="destructive" size="icon" onClick={() => deleteExpense(expense.id)}>
                    <TrashIcon className="h-4 w-4" />
                  </Button>
                </div>
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Total Expenses</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-2xl font-bold">${totalExpenses.toFixed(2)}</p>
        </CardContent>
      </Card>
    </div>
  )
}
